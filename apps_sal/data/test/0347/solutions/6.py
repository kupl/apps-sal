max_scores = [ 500, 1000, 1500, 2000, 2500 ]
corects = [ int(c) for c in input().split() ]
wrongs = [ int(w) for w in input().split() ]
shacks, unshacks = map(int, input().split())
final_score = shacks*100 - unshacks*50

def score(x, m, w):
  return max(0.3*x, (1-(m/250))*x-50*w)

for i in range(5):
  final_score += score(max_scores[i], corects[i], wrongs[i])
print(int(final_score))
