N = int(input())
a = list(map(int, input().split()))
color = set()
rainbow = 0

for n in range(N):
  if 1 <= a[n] < 400:
    color.add("gray")
  elif 400 <= a[n] < 800:
    color.add("brown")
  elif 800 <= a[n] < 1200:
    color.add("green")
  elif 1200<= a[n] < 1600:
    color.add("water")
  elif 1600 <= a[n] < 2000:
    color.add("blue")
  elif 2000 <= a[n] < 2400:
    color.add('yellow')
  elif 2400 <= a[n] < 2800:
    color.add('orange')
  elif 2800 <= a[n] < 3200:
    color.add('red')
  else:
    rainbow += 1

if len(color) == 0:
	color_min = 1 
	color_max = rainbow
else:
  color_min = len(color)
  color_max = color_min + rainbow

    
print(f'{color_min} {color_max}')

