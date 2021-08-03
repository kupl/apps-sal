N = int(input())
A = list(map(int, input().split()))

maxn = 1000005
prime = [0 for _ in range(maxn)]

for i in range(2, maxn):
    if prime[i] == 0:
        for j in range(i, maxn, i):
            prime[j] = i  # 最大質因數

st = set()  # 目前出現過的所有質因數，一開始為A[0]的所有質因數
a = A[0]
while prime[a]:
    st.add(prime[a])
    x = prime[a]
    while (a % x == 0):
        a //= x

pairwise = True
st2 = st  # 所有數共有的質因數，一開始為A[0]的所有質因數
for a in A[1:]:
    tmp = set()
    for j in st2:
        if a % j == 0:
            tmp.add(j)

    st2 = tmp
    if pairwise:
        while prime[a]:
            if prime[a] in st:
                pairwise = False
            st.add(prime[a])
            x = prime[a]
            while (a % x == 0):
                a //= x

if pairwise:
    print("pairwise coprime")
elif len(st2) == 0:
    print("setwise coprime")
else:
    print("not coprime")
