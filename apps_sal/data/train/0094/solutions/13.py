import os
from sys import stdin, stdout

class Input:
    def __init__(self):
        self.lines = stdin.readlines()
        self.idx = 0
    
    def line(self):
        try:
            return self.lines[self.idx].strip()
        finally:
            self.idx += 1
    
    def array(self, sep = ' ', cast = int):
        return list(map(cast, self.line().split(sep = sep)))
    
    def known_tests(self):
        num_of_cases, = self.array()
    
        for case in range(num_of_cases):
            yield self
    
    def unknown_tests(self):
        while self.idx < len(self.lines):
            yield self

def problem_solver():
    '''
    
    '''
    def solver(inpt):
        n, T = inpt.array()
        a = inpt.array()
        b = []
        c = 0

        for x in a:
            if x * 2 > T:
                b.append(1)
            elif x * 2 == T:
                b.append(c & 1)
                c += 1
            else:
                b.append(0)
        
        print(*b)

    '''Returns solver'''
    return solver

try:
    solver = problem_solver()
    for tc in Input().known_tests():
        solver(tc)
except Exception as e:
    import traceback
    traceback.print_exc(file=stdout)
