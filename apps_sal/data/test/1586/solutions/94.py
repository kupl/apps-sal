n = int(input())

if(n % 2 !=0):
    print(0)
    return

ketasu = len(str(n))

ans = 0
for i in range(1, 100):
    ans += n // (2 * 5 **i)

print(ans)
