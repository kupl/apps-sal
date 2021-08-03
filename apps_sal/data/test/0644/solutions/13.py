t = int(input())
st = [1]
x = 0
OVER = (1 << 32) - 1
for _ in range(t):
    command = input().split(" ")
    if command[0] == "add":
        x += st[-1]
        if x > OVER:
            print("OVERFLOW!!!")
            return
    elif command[0] == "for":
        number = int(command[1])
        st.append(min(OVER + 1, st[-1] * number))
    elif command[0] == "end":
        st.pop(-1)
print(x)
