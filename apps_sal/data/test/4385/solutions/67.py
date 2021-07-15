from itertools import combinations
def test():
  num_list = [int(input()) for _ in range(5)]
  k=int(input())
  l=list(combinations(num_list,2))
  for i,j in l:
    if abs(i-j) >k:
      print(":(")
      return
  print("Yay!")
test()
