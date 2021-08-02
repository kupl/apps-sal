st = input()
x = st.count('a')
y = len(st) - x
while x <= y:
    y -= 1
print(x + y)
