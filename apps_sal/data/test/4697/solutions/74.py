n, m = map(int, input().split())
m = (m//2) * 2
if n > m//2:
    print(m//2)
else:
    print(n+(m-n*2)//4)
