N = int(input())
li_ = []
for i in range(N):
    A, B = list(map(int, input().split()))
    li_.append((B, A))
li_.sort()
time = 0
for i in range(N):
    time += li_[i][1]
    if time > li_[i][0]:
        print("No")
        return
print("Yes")
