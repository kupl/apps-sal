import sys
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
c2 = 0
speed = 0
c = 0
st = []

for i in a:
    if i[0] == 1:
        speed = i[1]
        while len(st) and st[-1] < speed:
            c += 1
            st.pop()
    elif i[0] == 2 and c2 > 0:
        c += c2
        c2 = 0
    elif i[0] == 3:
        st.append(i[1])
        while len(st) and st[-1] < speed:
            c += 1
            st.pop()
    elif i[0] == 4:
        c2 = 0
    elif i[0] == 5:
        st = []
    elif i[0] == 6:
        c2 += 1
print(c)
        

