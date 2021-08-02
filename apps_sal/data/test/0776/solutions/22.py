a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

n = int(input())

usb = []
ps = []

for i in range(n):
    x = input().split()

    if x[1] == "USB":
        usb.append(int(x[0]))
    else:
        ps.append(int(x[0]))

usb.sort()
usb.reverse()
ps.sort()
ps.reverse()

usb_k = min(a, len(usb))
ps_k = min(b, len(ps))


price = 0


for i in range(usb_k):
    price += usb.pop()


for i in range(ps_k):
    price += ps.pop()

usb.extend(ps)
usb.sort()
usb.reverse()

k = min(c, len(usb))

for i in range(k):
    price += usb.pop()

k = k + usb_k + ps_k

print(k, price)
