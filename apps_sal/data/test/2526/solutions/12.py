import numpy as np

x, y, a, b, c = map(int, input().split())

p = np.array(list(map(int, input().split())))
q = np.array(list(map(int, input().split())))
r = np.array(list(map(int, input().split())))

p.sort()
q.sort()
r.sort()

ans = p[-x:].sum()+q[-y:].sum()

p_cnt = 0
q_cnt = 0
r_cnt = 0
while not(-x+p_cnt == 0 and -y+q_cnt == 0) and -1-r_cnt >= -c:
  if -x+p_cnt == 0:
    if r[-1-r_cnt] > q[-y+q_cnt]:
      ans += r[-1-r_cnt] - q[-y+q_cnt]
      q_cnt += 1
      r_cnt += 1
    else:
      break
  
  elif -y+q_cnt == 0:
    if r[-1-r_cnt] > p[-x+p_cnt]:
      ans += r[-1-r_cnt] - p[-x+p_cnt]
      p_cnt += 1
      r_cnt += 1
    else:
      break

  elif p[-x+p_cnt] <= q[-y+q_cnt] and r[-1-r_cnt] > p[-x+p_cnt]:
    ans += r[-1-r_cnt] - p[-x+p_cnt]
    p_cnt += 1
    r_cnt += 1

  elif p[-x+p_cnt] > q[-y+q_cnt] and r[-1-r_cnt] > q[-y+q_cnt]:
    ans += r[-1-r_cnt] - q[-y+q_cnt]
    q_cnt += 1
    r_cnt += 1

  else:
    break

print(ans)
