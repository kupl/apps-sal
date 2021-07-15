n = int(input())
rang = list(range(2,n//2+1))
a = [i*(n//i-1) for i in rang]
print(sum(a)*4)

