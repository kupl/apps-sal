class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
      already_happy = sum(c for c, h in zip(customers, grumpy) if not h)
      
      running = sum(c for c, h in zip(customers[:X], grumpy[:X]) if h)
      
      max_happy = running
      for i in range(1, len(customers) - X + 1):
        if grumpy[i - 1] == 1:
          running -= customers[i - 1]
        if grumpy[i + X - 1] == 1:
          running += customers[i + X - 1]
        max_happy = max(running, max_happy)  
      
      return max_happy + already_happy
          

