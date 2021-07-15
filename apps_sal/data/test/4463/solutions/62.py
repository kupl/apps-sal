s = input()
t = input()

sorted_s = sorted(s)
sorted_t = sorted(t, reverse=True)

#print(sorted_s)
#print(sorted_t)

if sorted_s < sorted_t:
    print("Yes")
else:
    print("No")


