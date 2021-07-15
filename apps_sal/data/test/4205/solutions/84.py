N = int(input())
vec = list(map(int,input().split()))
vec2 = [i for i in vec]
vec2.sort()
cnt = 0
for i in range(N):
    cnt += vec[i] != vec2[i]
if cnt <= 2:
    print("YES")
else:
    print("NO")
