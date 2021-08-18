s = input()
t = input()

sorted_s = sorted(s)
sorted_t = sorted(t, reverse=True)


if sorted_s < sorted_t:
    print("Yes")
else:
    print("No")
