def is_regular_angle(angle: int) -> int:
    return 1 if (360 % (180 - angle)) == 0 else 0

n = int(input())
messages = ['NO', 'YES']

for _ in range(n):
    print(messages[is_regular_angle(int(input()))])
