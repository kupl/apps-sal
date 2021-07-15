class Solution:
    
    def createAscGraph(self, ratings):
        graph = {}
        for index, rating in enumerate(ratings):
            graph[rating] = []
            for rate in ratings[index + 1:]:
                if rate > rating:
                    graph[rating] += [rate]
        return graph
        
    def createDescGraph(self, ratings):
        graph = {}
        for index, rating in enumerate(ratings):
            graph[rating] = []
            for rate in ratings[index + 1:]:
                if rate < rating:
                    graph[rating] += [rate]
        return graph
    
    def count_sequences(self, graph):
        counter = 0
        for key in graph.keys():
            for item in graph[key]:
                for item in graph[item]:
                    counter += 1
                    
        return counter
    
    def numTeams(self, rating: List[int]) -> int:
        asc_graph = self.createAscGraph(rating)
        desc_graph = self.createDescGraph(rating)
        
        return self.count_sequences(asc_graph) + self.count_sequences(desc_graph)
