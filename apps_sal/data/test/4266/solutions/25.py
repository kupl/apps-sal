K, X = list(map(int,input().split()))
num = []

for i in range(X - (K -1), X + (K - 1) + 1):
    num.append(i)

num_str = [str(n) for n in num]

num = " ".join(num_str)
print(num)

