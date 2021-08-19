n = int(input())
s = list(input())
Four = ['P', 'Y', 'G', 'W']
ml = all((word in s for word in Four))
if ml:
    print('Four', flush=True)
else:
    print('Three', flush=True)
