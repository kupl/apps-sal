n = int(input())
b = list(map(int, input().split()))
c = dict()
# fdp=4*(10**5)
for i in range(n):
    bi = b[i]
    df = bi - (i + 1)
    # print(i,df)
    # print(df+fdp-1)
    c[df] = c.get(df, 0) + i + 1 + df
    # c[df+fdp-1]+=i+1+df
print(max(c.values()))
