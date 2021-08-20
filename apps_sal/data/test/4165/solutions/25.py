N = int(input())
widths = list(map(int, input().split()))
Notmax_widths = sum(widths) - max(widths)
result = 'Yes' if Notmax_widths > max(widths) else 'No'
print(result)
