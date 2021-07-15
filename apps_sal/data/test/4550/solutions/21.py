a, b, c = map(int, input().split())
jdg = False
if a + b == c: jdg = True
if b + c == a: jdg = True
if c + a == b: jdg = True
print( 'Yes' if jdg else 'No')
