s = input()
t = input()
ans = len(t)

for i in range(len(s) - len(t) + 1):
    w = 0
    # print("--"*t_length)
    #print(s[i:i+t_length], t, sep="\n")

    for k in range(len(t)):
        if s[i+k] != t[k]:
            w += 1
        """
            print("x", end="")
        else:
            print(" ", end="")
        """
    ans = min(ans, w)
    #print("\nw =", w, "ans = ", ans)

print(ans)

