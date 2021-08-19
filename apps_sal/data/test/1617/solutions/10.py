import math
n = int(input())
st = set([])
for i in range(1, int(math.sqrt(n)) + 2):
    if not n % i:
        k = i
        st.add(k * (n // k - 1) * (n // k) // 2 + n // k)
        k = n // i
        st.add(k * (n // k - 1) * (n // k) // 2 + n // k)
print(*sorted(list(st)))
