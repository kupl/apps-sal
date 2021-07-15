ipp = input()
n = [int(x) for x in ipp]
harshad = 0

for i in range(0, len(n)):
    harshad += n[i]

if int(ipp) % harshad == 0:
    print("Yes")
elif int(ipp) % harshad != 0:
    print("No")
