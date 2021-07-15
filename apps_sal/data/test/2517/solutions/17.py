def main():
  import numpy as np
  import itertools
  from scipy.sparse import csr_matrix
  from scipy.sparse.csgraph import floyd_warshall
  import sys
  readline = sys.stdin.readline
  readlines = sys.stdin.readlines

  N, M, R= map(int, readline().split())
  r = list(map(int,input().split()))
  lines = readlines()
  edge = np.array([line.split() for line in lines], dtype = np.int64).T
  graph = csr_matrix((edge[2], (edge[:2] - 1)), (N, N))
  distance_mat = floyd_warshall(graph,directed = False)
  #print(distance_mat)
  ans = float("inf")
  for town in itertools.permutations(r,R):
    #print(town)
    tmp = 0
    for i in range(R-1):
      tmp += distance_mat[town[i]-1][town[i+1]-1]
    ans = min(ans,tmp)
  print(int(ans))
main()
