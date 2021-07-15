S = input()
N = len(S)

# 10 ** 100は偶数。
# N - 1回移動すれば必ず定位置になるため、その後偶数回の移動は省略可能。
# 従い、N - 1回 or N回の移動で、偶数であるほうが答えの移動回数となる

K = 0
if (N - 1) % 2 == 0:
  K = N - 1
else:
  K = N
  
# step[i] = 各マスから次の移動先のマス
step = [0] * N
for i in range(N):
  if S[i] == "R":
    step[i] = i + 1
  else:
    step[i] = i - 1
    
ans = [1] * N
while K:
  if K & 1:
    new_ans = [0] * N
    for i in range(len(step)):
      new_ans[step[i]] += ans[i]
    ans = new_ans
    
  step = [step[step[i]] for i in range(N)]
  K >>= 1

print(*ans)
