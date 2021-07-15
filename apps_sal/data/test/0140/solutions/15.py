def readint():
  return int(input())

def readlistint():
  return list(map(int, input().split()))

def readgridint(rows):
  grid = []
  for idx in range(rows):
    col = list(map(int, input().split()))
    grid.append(col)
  
  return grid

antennas = []
total_len = -1
memo = {}
def solve(left, idx):
  if(left > total_len):
    return 0
  key = (left, idx)
  if(key in memo):
    return memo[key]
  if(idx == len(antennas) - 1):
    ret = max(0, max(antennas[idx][0] - left, total_len - antennas[idx][1]))
    #print(left, idx, ret)
    memo[key] = ret
    return ret
  else:
    best = solve(left, idx + 1)
    best = min(best, max(0, max(antennas[idx][0] - left, total_len - antennas[idx][1])))
    added = max(antennas[idx][0] - left, 0)
    best = min(best, added + solve(antennas[idx][1] + added + 1, idx+1))
    memo[key] = best
    return best
    
def main():
  nonlocal total_len
  N, L = readlistint()
  total_len = L
  for idx in range(N):
    pos, R = readlistint()
    antennas.append([pos-R, pos + R])
  
  antennas.sort()
  #print(total_len, antennas)
  #ret = solve(1, 0)
  #print(ret)
  
  INF = 100000000000
  dp = [INF]*(total_len + 10)
  dp[0] = 0
  for ant in antennas:
    ant_left, ant_right = ant
    for idx in range(0, total_len + 1):
      if(dp[idx] == INF):
        continue
      dp[total_len] = min(dp[total_len], dp[idx] + max(0, max(ant_left - idx - 1, total_len - ant_right)))
      added = max(ant_left - idx - 1, 0)
      right_point = min(total_len, ant_right + added)
      dp[right_point] = min(dp[right_point], dp[idx] + added)
  
  print(dp[total_len])
  


main()
