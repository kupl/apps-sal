n = int(input())
A = [i for i in range(1, n+1, 2)]
B = [i for i in range(n-2 if n%2 else n-1, 0, -2)]
C = [i for i in range(2, n+1, 2)]
D = [i for i in range(n-1 if n%2 else n-2, 0, -2)]
ans = ' '.join(map(str, A+B+C+D+[n]))
print(ans)

