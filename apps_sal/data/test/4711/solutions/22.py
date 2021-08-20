(a, b, c) = map(int, input().split())
bell_list = []
bell_list.append(a + b)
bell_list.append(b + c)
bell_list.append(a + c)
print(min(bell_list))
