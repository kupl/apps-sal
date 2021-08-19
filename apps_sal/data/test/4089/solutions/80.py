from collections import deque
n = int(input())
st = deque()
while n > 0:
    num = (n - 1) % 26
    n = (n - 1) // 26
    st.appendleft(chr(num + 97))
print(*st, sep='')
