USBs = int(input())
fileSize = int(input())
USBList = []
for USB in range(USBs):
    USBList.append(int(input()))

USBCount = 0
storedAmount = 0
while storedAmount < fileSize:
    USBCount += 1
    currentUSB = max(USBList)
    storedAmount += currentUSB
    USBList.remove(currentUSB)

print(USBCount)
