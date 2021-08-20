s = input()
t = input()
print(sum((s_ == t_ for (s_, t_) in zip(s, t))))
