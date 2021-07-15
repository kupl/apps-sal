__author__ = 'zihaozhu'
from sys import stdin

USBOnly, UpsOnly, either = map(int, stdin.readline().split())
options = int(stdin.readline().rstrip())

usb = []
ups = []
for i in range (options):
    ip = stdin.readline().split()
    if ip[1] == "USB":
        usb.append(int(ip[0]))
    else:
        ups.append(int(ip[0]))

usb.sort()
ups.sort()
numMouse = 0
cost = 0
usbCnt = 0
upsCnt = 0
while USBOnly>0 and usbCnt<len(usb):
    cost+=usb[usbCnt]
    usbCnt+=1
    USBOnly-=1
    numMouse+=1

while UpsOnly>0 and upsCnt<len(ups):
    cost+=ups[upsCnt]
    upsCnt+=1
    UpsOnly-=1
    numMouse+=1

while either>0 and (usbCnt<len(usb) or upsCnt<len(ups)):
    either-=1
    val1 = float('inf')
    val2 = float('inf')
    if usbCnt<len(usb):
        val1 = usb[usbCnt]
        #usbCnt+=1
    if upsCnt<len(ups):
        val2 = ups[upsCnt]
        #upsCnt+=1
    numMouse+=1
    minVal = min(val1,val2)
    if minVal == val1:
        usbCnt+=1
    elif minVal == val2:
        upsCnt+=1
    cost+=min(val1,val2)


print("%s %s"% (numMouse, cost))
