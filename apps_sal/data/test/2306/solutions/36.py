n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))
runtime = sum(t)
speed = [0] * (runtime*2+1)
now_t, now_v = 0,0
for ti,vi in zip(t,v):
  for i in range(now_t*2+1,now_t*2+ti*2+1):
    next_v = min(now_v+0.5, vi)
    speed[i] = next_v
    now_v = next_v
  now_t += ti
speed[-1] = 0
now_t, now_v = runtime,0
for ti,vi in zip(t[::-1],v[::-1]):
  for i in range(now_t*2-1,now_t*2-ti*2-1,-1):
    next_v = min([now_v+0.5, speed[i],vi])
    speed[i] = next_v
    now_v = next_v
  now_t -= ti
ans = 0
for i in range(runtime*2):
  ans += speed[i]+speed[i+1]
ans /= 4
print(ans)
