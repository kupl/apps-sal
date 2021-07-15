def get_gcd(a, b):
    if a<b:a,b=b,a
    if b == 0 :return a
    else:return get_gcd(b,a%b)

n = int(input().rstrip())
a = list(map(int,input().rstrip().split()))

gcd = a[0]
for i in range(1,n):
    gcd = get_gcd(gcd,a[i])
print(gcd)
