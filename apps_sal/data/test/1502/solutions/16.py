# bits = list(map(int, bin(int(input()))[2:]))
# while len(bits) < 4:
    # bits.append(0)

# bits = [bits[0], bits[1] ^ bits[0], bits[2] ^ (bits[1] | bits[0]), bits[3] ^ (bits[0] | bits[1] | bits[2])]

# print(bits[0] + bits[1] * 2 + bits[2] * 4 + bits[3] * 8)

r = int(input())
if r == 0:
     print(15)
elif r == 1:
    print(14)
elif r == 2:
    print(12)
elif r == 3:
     print(13)
elif r == 4:
     print(8)
elif r == 5:
    print(9)
elif r == 6:
    print(10)
elif r == 7:
    print(11)
elif r == 8:
    print(0)
else:
    print(r - 8)

