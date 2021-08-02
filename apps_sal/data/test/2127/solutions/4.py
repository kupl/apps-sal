n = int(input())

mini = -1
maxi = -1

ans_arr = []

for t in range(n):
    [a, b, c] = input().split()

    b = int(b)
    c = int(c)

    if(a == "+"):
        v1 = min(b, c)
        v2 = max(b, c)
        if(v1 > mini):
            mini = v1
        if(v2 > maxi):
            maxi = v2
    else:
        if((mini <= b and maxi <= c) or (mini <= c and maxi <= b)):
            ans_arr.append("YES")
        else:
            ans_arr.append("NO")

for k in range(len(ans_arr)):
    print(ans_arr[k])
