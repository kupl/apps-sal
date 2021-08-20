(a, b, c) = map(int, input().split())
n = int(input())
mice_usb = []
mice_ps = []
for i in range(n):
    (price, mice_type) = input().split()
    if mice_type[0] == 'U':
        mice_usb.append(int(price))
    else:
        mice_ps.append(int(price))
usb = min(len(mice_usb), a)
ps2 = min(len(mice_ps), b)
mice_usb.sort()
mice_ps.sort()
answer = sum(mice_usb[:usb]) + sum(mice_ps[:ps2])
num = usb + ps2
left = mice_usb[usb:] + mice_ps[ps2:]
left.sort()
any_num = min(len(left), c)
answer += sum(left[:any_num])
num += any_num
print(num, answer)
