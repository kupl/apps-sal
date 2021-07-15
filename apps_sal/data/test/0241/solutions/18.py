n, m, Min, Max = map(int, input().split())
a = list(map(int, input().split()))
remain = n - m
cnt = 0
flag = 0
for i in a:
    if i == Min or i == Max:
        cnt += 1
    if i < Min or i > Max:
        flag = -1
cnt = 2 - cnt
if flag == -1:
    print("Incorrect")
elif n - m >= cnt:
    print("Correct")
else:
    print("Incorrect")
