angle = int(input())
angle = (angle % 360 + 360) % 360
angle = (angle + 44) % 360
answer = (angle % 359) // 90
print(answer)
