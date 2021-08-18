L = int(input())
A = int(input())
l1 = []
D = A
s1 = str(D)
"""
while True:
	if (D<10):
		l1.append(D)
		s1+=str(D)
		break
	else:
		l1.append(D%10)
		s1+=str(D%10)
		D=D//10

"""
q = len(s1) // L
q1 = q + 1
if (len(s1) % L != 0):
    print(("1" + "0" * (L - 1)) * q1)
else:
    s = ""
    if (L == len(s1)):
        print(A + 1)
    elif (int(s1[0]) < int(s1[L])):
        v = s1[0:L]
        s += v[0:len(v) - 1]
        s += str(int(v[-1]) + 1)
        print(s * q)

    else:
        l2 = []
        ind = 0
        for m in range(q):
            l2.append(int(s1[ind:ind + L]))
            ind = ind + L
        c = l2[0]
        val = 0
        for j in l2:
            if j > c:
                c += 1
                break
            elif j == c:
                val += 1
        if val == len(l2):
            d = c + 1
            d = str(d)
            if (len(str(d)) > len(str(c))):
                c = d[0:len(d) - 1]
                q += 1
            else:
                c = str(d)
        print(str(c) * q)
