a, b, c = map(int, input().split())
m = int(input())
usb = []
ps = []
for i in range(m):
    val, name = input().split()
    if name == 'USB':
        usb.append(int(val))
    else:
        ps.append(int(val))
usb.sort()
ps.sort()
sum1 = sum(usb[:min(len(usb), a)])
sum2 = sum(ps[:min(len(ps), b)])
u1 = min(len(usb), a)
u2 = min(len(ps), b)
usbps = usb[min(len(usb), a):] + ps[min(len(ps), b):]
usbps.sort()
sum3 = sum(usbps[:min(len(usbps), c)])
u3 = min(len(usbps), c)
print(u1 + u2 + u3, sum1 + sum2 + sum3)
