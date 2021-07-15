def check(a):
    if len(a) < 5:
        return 0
    does_have_little = 0
    for elem in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
        if elem in a:
            does_have_little = 1
            break
    if not does_have_little:
        return 0
    does_have_big = 0
    for elem in [chr(i) for i in range(ord('A'), ord('Z') + 1)]:
        if elem in a:
            does_have_big = 1
            break
    if not does_have_big:
        return 0
    number = 0
    for elem in [chr(i) for i in range(ord('0'), ord('9') + 1)]:
        if elem in a:
            number = 1
            break
    if not number:
        return 0
    return 1

a = input()
if check(a):
    print("Correct")
else:
    print("Too weak")
