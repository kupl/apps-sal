r, g, b = map(str, input().split())

number = r + g + b
print("YES" if int(number) % 4 == 0 else "NO")
