def func():
    visited = set()
    next_char = ord('a')
    for c in input():
        if c not in visited:
            if ord(c) != next_char:
                print('NO')
                return
            else:
                visited.add(c)
                next_char += 1
    print('YES')


func()
