def pflag(flag):
    if flag:
        return "odd"
    else:
        return "even"


n = int(input())
arr = list(map(int, (input()).split()))
m = int(input())
flag = False

# current parity
count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[j] < arr[i]:
            count += 1
if count % 2 == 0:
    flag = False
else:
    flag = True
# print("nothing")
# print(flag)

newflag = 0
ans = []
for i in range(m):
    l, r = map(int, input().split())
    e = (r - l + 1) // 2
    if e % 2 == 0:
        newflag = False
    else:
        newflag = True
    #print("new flag ", newflag)
    if flag and newflag or not flag and not newflag:
        flag = False  # even
        ans.append("even")
    else:
        flag = True  # odd
        ans.append("odd")

    # print(pflag(flag))

print("\n".join(ans))
