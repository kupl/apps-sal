problems = [ 500, 1000, 1500, 2000, 2500 ]
submitted = list(map(int, input().split()))
wrong = list(map(int, input().split()))

score = 0
for pos, x in enumerate(problems):
    m = submitted[pos]
    w = wrong[pos]
    score += max( 3 * x // 10,  x - m * x // 250 - 50 * w )

good, bad = list(map(int, input().split()))
score += good * 100 - bad * 50

print(score)

