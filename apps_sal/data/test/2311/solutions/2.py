n, m, k = map(int, input().split())
a = input().split()
b = input().split()
ans = 0
for i in range(1, int(k**0.5) + 1):
    if(k % i == 0):
        f1 = i
        f2 = k // i
        if(f1 != f2):
            temp1 = 0
            count = 0
            for j in range(n):
                if(a[j] == '1'):
                    count += 1
                else:
                    count = 0
                if(count >= f1):
                    temp1 += 1
            temp2 = 0
            count = 0
            for j in range(m):
                if(b[j] == '1'):
                    count += 1
                else:
                    count = 0
                if(count >= f2):
                    temp2 += 1
            ans += temp1 * temp2
            temp1 = 0
            count = 0
            for j in range(n):
                if(a[j] == '1'):
                    count += 1
                else:
                    count = 0
                if(count >= f2):
                    temp1 += 1
            temp2 = 0
            count = 0
            for j in range(m):
                if(b[j] == '1'):
                    count += 1
                else:
                    count = 0
                if(count >= f1):
                    temp2 += 1
            ans += temp1 * temp2
        else:
            temp1 = 0
            count = 0
            for j in range(n):
                if(a[j] == '1'):
                    count += 1
                else:
                    count = 0
                if(count >= f1):
                    temp1 += 1
            temp2 = 0
            count = 0
            for j in range(m):
                if(b[j] == '1'):
                    count += 1
                else:
                    count = 0
                if(count >= f2):
                    temp2 += 1
            ans += temp1 * temp2
print(ans)
