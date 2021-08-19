(n, k) = input().split(' ')
n = int(n)
k = int(k)
y = [int(x) for x in input().split(' ')]
teams = 0
st = []
for x in y:
    if 5 - x >= k:
        st.append(x)
teams = len(st) // 3
print(teams)
