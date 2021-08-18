n = int(input())
speed = 0
overtake_allowed = True
just_overtake_violation = False
speed_signs = []
violations = 0
overtake_passed = 0
for i in range(n):
    arr = [int(a) for a in input().split(' ')]

    if arr[0] == 1:
        if arr[1] > speed:
            speed = arr[1]
            for j in range(len(speed_signs) - 1, -1, -1):
                if speed > speed_signs[j]:
                    violations += 1
                    del speed_signs[j]
                else:
                    break
        else:
            speed = arr[1]

    if arr[0] == 2:
        violations += overtake_passed
        overtake_passed = 0

    if arr[0] == 3:
        if speed > arr[1]:
            violations += 1
        else:
            speed_signs.append(arr[1])

    if arr[0] == 4:
        overtake_passed = 0

    if arr[0] == 5:
        speed_signs = []

    if arr[0] == 6:
        overtake_passed += 1
print(violations)
